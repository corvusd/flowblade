"""
    Flowblade Movie Editor is a nonlinear video editor.
    Copyright 2023 Janne Liljeblad.

    This file is part of Flowblade Movie Editor <https://github.com/jliljebl/flowblade/>.

    Flowblade Movie Editor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Flowblade Movie Editor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Flowblade Movie Editor. If not, see <http://www.gnu.org/licenses/>.
"""

"""
This module handles creating data folders for individual projects data files and providing 
access to them for all later saved versions of the initial project. 
"""

from gi.repository import GLib
import os

from editorstate import PROJECT


# User folder locations
_xdg_config_dir = None
_xdg_data_dir = None
_xdg_cache_dir = None
    
# The one projects data folder quaranteed to always exist and the default one
# until user creates a new one and sets it active. 
DEFAULT_PROJECTS_DATA_FOLDER = "projectsdata"

# Project data folders
THUMBNAILS_FOLDER = "thumbnails/"
RENDERS_FOLDER = "rendered_clips/"
CONTAINER_CLIPS_FOLDER = "container_clips/"
CONTAINER_CLIPS_UNRENDERED = "container_clips/unrendered/"
AUDIO_LEVELS_FOLDER = "audio_levels/"
PROXIES_FOLDER = "proxies/"

# ------------------------------------------------------------------------ init
def init():
    # This data is duplicated with userfolders.py but thats really not an issue.
    global _xdg_config_dir, _xdg_data_dir, _xdg_cache_dir

    # XDG folders
    _xdg_config_dir = os.path.join(GLib.get_user_config_dir(), "flowblade")
    _xdg_data_dir = os.path.join(GLib.get_user_data_dir(), "flowblade")
    _xdg_cache_dir = os.path.join(GLib.get_user_cache_dir(), "flowblade")

    # This should only happen once omn first use of application.
    if not os.path.exists(get_active_vault_folder()):
        os.mkdir(get_active_vault_folder())

# --------------------------------------------------------- vault
def get_active_vault_folder():
    return _xdg_data_dir + "/" + DEFAULT_PROJECTS_DATA_FOLDER

# --------------------------------------------------------- data folders paths
def get_project_data_folder():
    path = PROJECT().vault_folder + "/" + PROJECT().project_data_id + "/"
    return path

def get_thumbnails_folder():
    return get_project_data_folder() + THUMBNAILS_FOLDER

def get_render_folder():
    return get_project_data_folder() + RENDERS_FOLDER

def get_containers_folder():
    return get_project_data_folder() + CONTAINER_CLIPS_FOLDER

def get_container_clips_unrendered_folder():
    return get_project_data_folder() + CONTAINER_CLIPS_UNRENDERED
    
def get_audio_levels_folder():
    return get_project_data_folder() + AUDIO_LEVELS_FOLDER

def get_proxies_folder():
    return get_project_data_folder() + PROXIES_FOLDER
    
# ----------------------------------------------------- functional methods
def create_project_data_folders():
    print(get_project_data_folder())
    
    os.mkdir(get_project_data_folder())
    os.mkdir(get_thumbnails_folder())
    os.mkdir(get_render_folder())
    os.mkdir(get_containers_folder())
    os.mkdir(get_container_clips_unrendered_folder())
    os.mkdir(get_audio_levels_folder())
    os.mkdir(get_proxies_folder())
