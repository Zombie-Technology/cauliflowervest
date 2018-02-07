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

"""Module to handle display of created passphrases."""

import datetime

from google.appengine.api import users

from cauliflowervest.server import permissions
from cauliflowervest.server import util
from cauliflowervest.server.handlers import base_handler
from cauliflowervest.server.models import base
from cauliflowervest.server.models import volumes as models

PROVISIONING_FILTER_SECONDS = 60 * 60 * 24


def ProvisioningVolumesForUser(user, time_s):
  """Find provisioning volumes, created by the user in the last n seconds.

  Args:
    user: users.user object of the user that created the secrets.
    time_s: integer, amount of seconds of time passed for query to filter
      through.
  Returns:
    list of entities created by user in the last n seconds.
  """

  query = models.ProvisioningVolume.all()

  time = datetime.datetime.now() - datetime.timedelta(seconds=time_s)
  query.filter('created_by' ' =', user).filter('created' ' >', time)
  volumes = query.fetch(999)
  volumes.sort(key=lambda x: x.created, reverse=True)
  return volumes


class Created(base_handler.BaseHandler):
  """Handler for /created URL."""

  def get(self):
    """Handles GET requests."""

    base_handler.VerifyPermissions(
        permissions.RETRIEVE_CREATED_BY,
        base.GetCurrentUser(),
        permissions.TYPE_PROVISIONING)

    volumes = ProvisioningVolumesForUser(users.get_current_user(),
                                         PROVISIONING_FILTER_SECONDS)
    volumes = [volume.ToDict() for volume in volumes]

    self.response.out.write(util.ToSafeJson(volumes))
