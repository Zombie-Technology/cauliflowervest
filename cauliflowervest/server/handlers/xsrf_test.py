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

"""xsrf module tests."""

import httplib



import mock

from absl.testing import absltest

from cauliflowervest import settings as base_settings
from cauliflowervest.server import main as gae_main
from cauliflowervest.server import util
from cauliflowervest.server.handlers import test_util
from cauliflowervest.server.models import base


class XsrfRequestHandlerTest(test_util.BaseTest):
  """Test for xsrf module."""



if __name__ == '__main__':
  absltest.main()
