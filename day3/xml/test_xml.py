from utilities import subprocess_runner


def test_xml_ex2():
    base_path = "."
    cmd_list = ["python", "ex2_jnpr_rpc.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)

    assert std_err == ""
    assert return_code == 0
    assert std_out.count("inet6") == 2
    assert std_out.count("inet") == 8
