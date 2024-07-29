from src.sample_code import print_message, print_message_from_env

def test_print_message_when_valid_message_should_print_message(capfd) -> None:
    print_message("teste")
    out, err = capfd.readouterr()
    assert out == "teste\n"

def test_print_message_from_env_when_valid_config_should_print_message(capfd) -> None:
    print_message_from_env()
    out, err = capfd.readouterr()
    assert out == "TEST ENV\n"