# load("@rules_python//python:defs.bzl", "py_binary", "py_test", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")
load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_pytest_main")

load("@rules_python//python:defs.bzl", "py_test")

py_library(
    name = "name",
    srcs = [
      "name.py",
    ],
    deps = [
      requirement("requests"),
    ],
)

py_binary(
  name = "main",
  srcs = [
    "main.py",
  ],
  main = "main.py",
  deps = [
    ":name",
  ],
)

py_pytest_main(name = "__test__")


py_test(
    name = "name_test",
    srcs = [
        "name_test.py",
        ":__test__"
    ],
    main = ":__test__.py",
    deps = [
        ":__test__",
        ":name",
        requirement("pytest"),
    ],
)
