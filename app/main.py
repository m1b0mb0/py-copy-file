def copy_file(command: str) -> None:
    command_len = len(command.split())
    if command_len == 3:
        command_name, original_file, new_file = command.split()
        if original_file != new_file and command_name == "cp":
            try:
                with (
                    open(original_file, "r") as file_in,
                    open(new_file, "w") as file_out
                ):
                    for line in file_in.readlines():
                        file_out.write(line)
            except FileNotFoundError as e:
                print(e)
