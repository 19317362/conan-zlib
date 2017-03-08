from conans.model.conan_file import ConanFile
from conans import CMake
import os

############### CONFIGURE THESE VALUES ##################
default_user = "lasote"
default_channel = "testing"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "zlib/1.2.11@%s/%s" % (username, channel)

    def build(self):
        cmake = CMake(self.settings)
        # Current dir is "test_package/build/{build_id}" and CMakeLists.txt is in "test_package"
        cmake.configure(self, source_dir="../../", build_dir="./")
        cmake.build(self)

        # self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.dylib", dst="bin", src="lib")
        
    def test(self):
        self.run("cd bin && .%senough" % os.sep)
