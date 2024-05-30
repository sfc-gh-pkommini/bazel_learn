load("@rules_python//python:defs.bzl", "py_binary")
load("@pip_deps//:requirements.bzl", "requirement")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "requirements",
    requirements_in = "//:requirements.in",
    requirements_txt = "//:requirements-lock.txt",
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        "//src:name",
    ],
)
