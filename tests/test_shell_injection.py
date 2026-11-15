"""Command injection regressiya testi (HIGH-002).

Muammo: `text_to_voice.py` `os.system()` orqali AI javobini (foydalanuvchi
ovozidan olingan matn) shell buyrug'iga to'g'ridan-to'g'ri qo'shar edi:

    os.system(f'edge-tts ... --text "{data}" ...')

`data` ichida `"` bo'lsa, shell buyrug'i buzilib, ixtiyoriy buyruq ishga
tushadi (masalan `"; touch PWNED; echo "`).

Bu test tuzatilgunga qadar YIQILADI.
"""
import ast
import os
import subprocess
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAYLOAD = 'x"; touch PWNED; echo "'


class ShellInjectionTest(unittest.TestCase):
    def test_command_built_as_argv_list(self):
        """Buyruq ro'yxat (argv) ko'rinishida qurilishi kerak — shell yo'q."""
        import text_to_voice

        cmd = text_to_voice.build_edge_tts_command(PAYLOAD, "out.mp3")
        self.assertIsInstance(cmd, list, "buyruq list bo'lishi kerak (shell=False)")
        self.assertIn(PAYLOAD, cmd, "xavfli matn bitta argv elementi bo'lishi kerak")

    def test_no_shell_metacharacter_interpretation(self):
        """Xavfli matn shell tomonidan bajarilmasligi kerak."""
        import text_to_voice

        marker = os.path.join(REPO_ROOT, "PWNED")
        if os.path.exists(marker):
            os.remove(marker)
        cmd = text_to_voice.build_edge_tts_command(PAYLOAD, "out.mp3")
        # /bin/echo bilan bir xil argv ni ishga tushiramiz — shell yo'q.
        subprocess.run(["/bin/echo"] + cmd[1:], capture_output=True)
        self.assertFalse(
            os.path.exists(marker),
            "xavfli matn shell buyrug'i sifatida bajarildi (command injection)",
        )

    def test_no_os_system_in_repo(self):
        """Repo'da os.system() ishlatilmasligi kerak."""
        offenders = []
        for root, dirs, files in os.walk(REPO_ROOT):
            dirs[:] = [d for d in dirs if d not in {".git", ".venv", "venv", "__pycache__", "tests"}]
            for name in files:
                if not name.endswith(".py"):
                    continue
                path = os.path.join(root, name)
                src = open(path, encoding="utf-8", errors="ignore").read()
                try:
                    tree = ast.parse(src)
                except SyntaxError:
                    continue
                for node in ast.walk(tree):
                    if (
                        isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Attribute)
                        and node.func.attr == "system"
                        and isinstance(node.func.value, ast.Name)
                        and node.func.value.id == "os"
                    ):
                        rel = os.path.relpath(path, REPO_ROOT)
                        offenders.append(f"{rel}:{node.lineno} os.system()")
        self.assertEqual(offenders, [], "os.system() topildi:\n" + "\n".join(offenders))


if __name__ == "__main__":
    unittest.main()
