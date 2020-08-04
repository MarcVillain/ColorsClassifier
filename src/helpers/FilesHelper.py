import imghdr
import logging
import os
import shutil

from src.helpers.IOHelper import IOHelper

logger = logging.getLogger()


class FilesHelper:
    @staticmethod
    def create_dir(path, force=False, ignore_errors=False):
        """
        Create a directory. If it already exists, ask for override.
        :param path: Path of the directory to create.
        :param force: If True, it will not ask for permission to override.
        :param ignore_errors: If True, fail without asking for override.
        :return: True if created else False.
        """
        # Ask for cleanup if necessary
        if os.path.exists(path):
            if not force:
                if ignore_errors:
                    return False
                print(f"Folder '{path}' already exists.")
                if not IOHelper.ask_yes_no("Do you want to replace it?"):
                    return False

            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path, ignore_errors=True)

        # Create directory
        try:
            os.mkdir(path)
        except OSError as e:
            logger.error(f"Creation of the directory '{path}' failed")
            logger.debug(e)
            return False

        return True

    @staticmethod
    def create_file(path, force=False):
        """
        Create an empty file. If it already exists, ask for override.
        :param path: Path of the file to create.
        :param force: If True, it will not ask for permission to override.
        :return: True if created else False.
        """
        # Ask for cleanup if necessary
        if os.path.exists(path):
            if not force:
                print(f"File '{path}' already exists.")
                if not IOHelper.ask_yes_no("Do you want to replace it?"):
                    return False
            shutil.rmtree(path, ignore_errors=True)

        # Create file
        try:
            with open(path, "w") as f:
                pass
        except OSError:
            logger.error(f"Creation of the file '{path}' failed")
            return False

        return True

    @staticmethod
    def get_images_in(folder):
        images = []
        for f in os.listdir(folder):
            file_path = os.path.join(folder, f)
            if not os.path.isfile(file_path):
                continue
            image_type = imghdr.what(file_path)
            if image_type is None:
                logger.debug(f"Not an image: {file_path}")
                continue
            images.append(file_path)
        return images

    @staticmethod
    def join(*args, **kwargs):
        return os.path.join(*args, **kwargs)

    @staticmethod
    def copy(src, dst):
        shutil.copyfile(src, dst)

    @staticmethod
    def basename(str):
        return os.path.basename(str)
