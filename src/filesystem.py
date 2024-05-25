
import time, os
import shutil


BOX_RETRIES = 3
BOX_RTM = 1

from src import *


BASE_FOLDER = 'box_data'

def _ensure_base_folder():
    if not os.path.exists(BASE_FOLDER):
        os.mkdir(BASE_FOLDER)


def create_folder(folder_name):
    """
    Creates a folder in the root folder given its name.
    :param folder_name: Folder name to create.
    :return: Folder identifier if the creation was successful, None otherwise.
    """
    
    for i in range(0, BOX_RETRIES):
        try:
            sub_folder = os.path.join(BASE_FOLDER, folder_name)
            os.mkdir(sub_folder)
            return sub_folder
        except Exception as e:
            time.sleep(BOX_RTM)
            if i == BOX_RETRIES - 1:
                print(f'Error creating the folder [{folder_name}] into folder root: {e}')
    return None


def create_shared_link(folder_id):
    """
    Creates an Internet accessible shared link of folder given its identifier.
    :param folder_id: Folder identifier.
    :return: Shared link if the creation was successful, None otherwise.
    """

    return None


def search_file(folder_id, file_name):
    """
    Finds a file into a folder given its identifier and a query string.
    :param folder_id: Folder identifier.
    :param file_name: File name.
    :return: File identifier if the file exists, None otherwise.
    """
    for i in range(0, BOX_RETRIES):
        try:
          folder = os.path.join(BASE_FOLDER, folder_id)
          for root, dirs, files in os.walk(folder):
            if file_name in files:
              return os.path.join(root, file_name)
            return None
        except Exception as e:
            time.sleep(BOX_RTM)
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API searching files into folder [{folder_id}] with name [{file_name}]: {e}')
    return None


def upload_file(folder_id, file_path):
    """
    Uploads a file (that must not exist in Box folder) into a folder given its path.
    :param folder_id: Folder identifier.
    :param file_path: File path.
    :return: File identifier if the upload was successful, None otherwise.
    """
    for i in range(0, BOX_RETRIES):
        try:
            file_name = file_path.split('/')[-1]
            shutil.copyfile(file_path, os.path.join(BASE_FOLDER, folder_id, file_name))
            return os.path.join(folder_id, file_name)
        except Exception as e:
            time.sleep(BOX_RTM)
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API uploading the file [{file_path}] to folder with id [{folder_id}]: {e}')
    return None


def update_file(file_id, file_path):
    """
    Updates a file (that must exist in Box folder) given its identifier.
    :param file_id: File identifier.
    :param file_path: File path.
    :return: File identifier if the update was successful, None otherwise.
    """
    for i in range(0, BOX_RETRIES):
        try:
            shutil.copyfile(file_path, os.path.join(file_id, file_path))
            return os.path.join(file_id, file_path)
        except Exception as e:
            time.sleep(BOX_RTM)
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API updating the file [{file_id}] with file [{file_path}]: {e}')
    return None


def download_file(file_id, file_path):
    """
    Downloads a Box file given its identifier to a specific path.
    :param file_id: File identifier.
    :param file_path: File path.
    :return: True if the download was successful, False otherwise.
    """
    for i in range(0, BOX_RETRIES):
        try:
            with open(file_path, 'wb') as file:
                shutil.copyfile(os.path.join(file_id, file_path), file_path)
            return True
        except Exception as e:
            time.sleep(BOX_RTM)
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API downloading the file [{file_id}] to file [{file_path}]: {e}')
    return False