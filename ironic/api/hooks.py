# -*- encoding: utf-8 -*-
#
# Copyright © 2012 New Dream Network, LLC (DreamHost)
#
# Author: Doug Hellmann <doug.hellmann@dreamhost.com>
#
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

from oslo.config import cfg
from pecan import hooks

from ironic.conductor import rpcapi
from ironic.db import api as dbapi
from ironic.openstack.common import context


class ConfigHook(hooks.PecanHook):
    """Attach the configuration object to the request
    so controllers can get to it.
    """

    def before(self, state):
        state.request.cfg = cfg.CONF


class DBHook(hooks.PecanHook):

    def before(self, state):
        state.request.dbapi = dbapi.get_instance()


class ContextHook(hooks.PecanHook):

    def before(self, state):
        # TODO(deva): Making all requests have admin context for early
        #             development. This needs to be fixed later!
        state.request.context = context.get_admin_context()


class RPCHook(hooks.PecanHook):

    def before(self, state):
        state.request.rpcapi = rpcapi.ConductorAPI()
