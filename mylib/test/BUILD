load("@aspect_rules_py//py:defs.bzl",  "py_pytest_main")
load("@rules_python//python:defs.bzl", "py_test")
load("@pypi//:requirements.bzl", "requirement")

py_pytest_main(name = "__test__")

py_test(
    name = "mylib_test",
    srcs = [
        "test.py",
        ":__test__",
    ],
    main = ":__test__.py",
    deps = [
        ":__test__",
        requirement("pytest"),
    ],
)
