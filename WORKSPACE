load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file")

# rules_python
http_archive(
    name = "rules_python",
    sha256 = "4912ced70dc1a2a8e4b86cec233b192ca053e82bc72d877b98e126156e8f228d",
    strip_prefix = "rules_python-0.32.2",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.32.2/rules_python-0.32.2.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")
py_repositories()
python_register_toolchains(
    name = "python_3_10",
    python_version = "3.10",
)

load("@python_3_10//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pypi",
    python_interpreter_target = interpreter,
    requirements_lock = "//:requirements-dev.txt",
)

load("@pypi//:requirements.bzl", install_pypi_deps = "install_deps")
install_pypi_deps()

# Aspect rules_py
http_archive(
    name = "aspect_rules_py",
    sha256 = "59446563a724b1cb449a604c8fbcd85e18a7001e9bb230ef59d78154886ad8cc",
    strip_prefix = "rules_py-0.7.3",
    url = "https://github.com/aspect-build/rules_py/releases/download/v0.7.3/rules_py-v0.7.3.tar.gz",
)

load("@aspect_rules_py//py:repositories.bzl", "rules_py_dependencies")
rules_py_dependencies()

load("@aspect_rules_py//py:toolchains.bzl", "rules_py_toolchains")
rules_py_toolchains()
