from app.config import load_config
from app.services.lean_service import run_lean_code

cfg = load_config()
print("Loaded config:", cfg)
# run with python -m app.main

lean_code = """
-- Define even as an inductive proposition
inductive even : Nat → Prop
| zero : even 0
| add_two {n : Nat} : even n → even (n + 2)

-- Theorem: n even → n + 2 even
theorem even_add_two {n : Nat} (h : even n) : even (n + 2) :=
  even.add_two h

-- Theorem: 0 + 2 + 2 is even
example : even (0 + 2 + 2) :=
  even.add_two (even.add_two even.zero)


"""

stdout, stderr = run_lean_code(lean_code)

print("STDOUT:", stdout)
print("STDERR:", stderr)
