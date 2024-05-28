load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_venv")
load("@pypi//:requirements.bzl", "requirement")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = ["//mylib:name"],
)

py_venv(
    name = "mylib_venv",
    venv_name = "mylib_venv",
    deps = [
        "//mylib:name",
        requirement("pytest"),
    ],
)
