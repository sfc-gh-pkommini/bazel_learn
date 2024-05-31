load("@rules_python//python:defs.bzl", "py_library", "py_test")
load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "name",
    srcs = ["name.py"],
    visibility = ["//visibility:public"],
    deps = [
        requirement("requests"),
    ]
)

py_test(
    name = "test",
    srcs = [
        "test.py",
    ],
    deps = [
        ":name",
        requirement("pytest"),
        requirement("requests"),
    ],
)
