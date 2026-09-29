def check_build(status):
    if status == "success":
        return "Build successful"
    else:
        return "Build failed"


print(check_build("success"))
