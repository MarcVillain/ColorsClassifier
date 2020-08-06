import imghdr
import logging
import os
import shutil

from colorsclassifier.src.helpers.IOHelper import IOHelper

logger = logging.getLogger("color_classifier")


class FilesHelper:
    """
    Helper class.

    Helps to handle files operations.
    """

    @classmethod
    def _clear_path(cls, path, force, ignore_errors):
        """
        Handle deletion of given path.
        :param path: File or folder to delete.
        :param force: If True, delete without any questions.
        :param ignore_errors: It True and not force, return False
        :return: True on success else False.
        """
        if os.path.exists(path):
            if not force:
                if ignore_errors:
                    return False
                # If directory, check if empty
                if os.path.isdir(path):
                    for _, _, files in os.walk(path):
                        if files and not IOHelper.ask_yes_no(
                            f"Folder '{path}' is not empty.\nDo you want to replace it?"
                        ):
                            return False
                        else:
                            break
                # If file, ask for replacement
                if os.path.isfile(path) and not IOHelper.ask_yes_no(
                    f"File '{path}' exists.\nDo you want to replace it?"
                ):
                    return False

            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path, ignore_errors=True)

    @classmethod
    def create_dir(cls, path, force=False, ignore_errors=False):
        """
        Create a directory. If it already exists, ask for override.
        :param path: Path of the directory to create.
        :param force: If True, it will not ask for permission to override.
        :param ignore_errors: If True, fail without asking for override.
        :return: True if created else False.
        """
        # Ask for cleanup if necessary
        cls._clear_path(path, force, ignore_errors)

        # Create directory
        try:
            os.mkdir(path)
        except OSError as e:
            logger.error(f"Creation of the directory '{path}' failed")
            logger.debug(e)
            return False

        return True

    @classmethod
    def create_file(cls, path, filename, force=False, ignore_errors=False):
        """
        Create an empty file. If it already exists, ask for override.
        :param path: Path of the file to create.
        :param filename: File name to use if path is a directory.
        :param force: If True, it will not ask for permission to override.
        :param ignore_errors: If True, fail without asking for override.
        :return: True if created else False.
        """
        # Ask for cleanup if necessary
        cls._clear_path(path, force, ignore_errors)

        # Create file
        if os.path.isdir(path):
            path = os.path.join(path, filename)
        try:
            with open(path, "w"):
                pass
        except OSError:
            logger.error(f"Creation of the file '{path}' failed")
            return False

        return True

    @staticmethod
    def get_images_in(folder, recurse=False):
        """
        List images files in given folder.
        :param folder: Look for images in this folder.
        :param recurse: If True, search recursively.
        :return: List of images paths.
        """
        if not folder or not os.path.exists(folder):
            return []

        images = []
        # TODO: Recursive search
        for f in os.listdir(folder):
            # Chek if file
            file_path = os.path.join(folder, f)
            if not os.path.isfile(file_path):
                continue
            # Check file type
            image_type = imghdr.what(file_path)
            if image_type is None:
                logger.debug(f"Not an image: {file_path}")
                continue
            # Add image path to list
            images.append(file_path)
        return images

    @staticmethod
    def join(*args, **kwargs):
        """
        Join path strings.
        Wrapper around os.path.join().
        :param args: Arguments.
        :param kwargs: Named arguments.
        :return: The joined path string.
        """
        return os.path.join(*args, **kwargs)

    @staticmethod
    def copy(src, dst):
        """
        Copy source to destination.
        Wrapper around shutil.copyfile().
        :param src: Source file or folder.
        :param dst: Destination file or folder.
        """
        shutil.copyfile(src, dst)

    @staticmethod
    def basename(path):
        """
        Get basename of path (aka filename).
        :param path: Path to manipulate.
        :return: Basename of the given path.
        """
        return os.path.basename(path)
