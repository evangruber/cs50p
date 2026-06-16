def main():
    file_name = input("File name: ").lower().replace(" ", "")

    file_name = get_file_ext(file_name)

    match file_name:
        case "gif":
            print("image/gif")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


def get_file_ext(file_name):
    if "." not in file_name:
        return file_name
    else:
        file_name, file_ext = file_name.split(".", 1)
        return get_file_ext(file_ext)


main()
