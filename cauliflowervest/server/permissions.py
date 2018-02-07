# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""App Engine Models for CauliflowerVest web application."""

RETRIEVE = 'retrieve'
RETRIEVE_OWN = 'retrieve_own'
RETRIEVE_CREATED_BY = 'retrieve_created_by'
ESCROW = 'escrow'
SEARCH = 'search'
MASTER = 'master'
SILENT_RETRIEVE_WITH_AUDIT_EMAIL = 'silent_retrieve'
SILENT_RETRIEVE = 'true_silent_retrieve'
CHANGE_OWNER = 'change_owner'

SET_REGULAR = (RETRIEVE, ESCROW, SEARCH, MASTER, CHANGE_OWNER)
SET_PROVISIONING = (RETRIEVE_CREATED_BY, SEARCH)
SET_SILENT_RETRIEVE_WITH_AUDIT_EMAIL = SET_REGULAR + (
    SILENT_RETRIEVE_WITH_AUDIT_EMAIL,)

SET_SILENT_RETRIEVE = SET_REGULAR + (SILENT_RETRIEVE,)

TYPE_BITLOCKER = 'bitlocker'
TYPE_DUPLICITY = 'duplicity'
TYPE_FILEVAULT = 'filevault'
TYPE_LUKS = 'luks'
TYPE_PROVISIONING = 'provisioning'
TYPE_APPLE_FIRMWARE = 'apple_firmware'
TYPE_LINUX_FIRMWARE = 'linux_firmware'
TYPE_WINDOWS_FIRMWARE = 'windows_firmware'
TYPES = [TYPE_BITLOCKER, TYPE_DUPLICITY, TYPE_FILEVAULT, TYPE_LUKS,
         TYPE_PROVISIONING, TYPE_APPLE_FIRMWARE, TYPE_LINUX_FIRMWARE,
         TYPE_WINDOWS_FIRMWARE]
