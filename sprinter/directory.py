"""
directory.py stores methodology to install various files and
packages to different locations.

"""
import os


class Directory(object):

    def __init__(self, namespace=None):
        """ takes in a namespace directory to initialize, defaults to .sprinter otherwise."""
        suffix = ("" if not namespace else "-%s" % namespace)
        self.root_dir = os.path.expanduser(os.path.join("~", ".sprinter%s" % suffix))
        self.__generate_dir(self.root_dir)

    def symlink_to_bin(self, name, path):
        """
        Symlink an object at path to name in the bin folder. remove it if it already exists.
        """
        self.__symlink_dir("bin", name, path)

    def symlink_to_lib(self, name, path):
        """
        Symlink an object at path to name in the lib folder. remove it if it already exists.
        """
        self.__symlink_dir("lib", name, path)

    def __generate_dir(self, root_dir):
        """ Generate the root directory root if it doesn't already exist """
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)
        assert os.path.isdir(self.root_dir), "%s is not a directory! Please move or remove it." % self.root_dir
        for d in ["bin", "lib"]:
            target_path = os.path.join(root_dir, d)
            if not os.path.exists(target_path):
                os.makedirs(target_path)

    def __symlink_dir(self, dir_name, name, path):
        """
        Symlink an object at path to name in the dir_name folder. remove it if it already exists.
        """
        target_path = os.path.join(self.root_dir, dir_name, name)
        if os.path.exists(target_path):
            assert not os.path.isdir(target_path), \
                "%s is not a symlink! please remove it manually." % target_path
            os.remove(target_path)
        os.symlink(path, target_path)