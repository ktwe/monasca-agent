# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import mock
import os
import subprocess
import unittest

from monasca_agent.collector.checks_d.elastic import ElasticSearch
from monasca_agent.common import util
from monasca_agent.collector.checks_d import ceph


class ElasticCheckTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        super(ElasticCheckTest, self).setUp()
        self.elastic_check = ElasticSearch('elastic', {'hostname': '127.0.0.1'}, {'version': '1.0.0'})
        self.base_url = 'http://localhost:9200'

    def test_version(self):
        version = self.elastic_check._get_es_version(self.base_url)

        self.assertEqual([5, 6, 14], version)

    def test_check(self):
        self.elastic_check.check({'url': self.base_url})
