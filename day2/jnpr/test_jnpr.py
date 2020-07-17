from utilities import subprocess_runner


def test_jnpr_ex1():
    base_path = "."
    cmd_list = ["python", "ex1_jnpr_facts.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)

    assert std_err == ""
    assert return_code == 0
    assert "VM5F0DDCE0AA" in std_out
    assert "vmx1" in std_out
