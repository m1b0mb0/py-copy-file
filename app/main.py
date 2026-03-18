def copy_file(command: str) -> None:
    splited_command = command.split()
    if len(splited_command) == 3:
        command_name, original_file, new_file = splited_command
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
