# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Abishek Subramanian, Cisco Systems, Inc.
# @author: Sergey Sudakovich,   Cisco Systems, Inc.

from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.router import dashboard


class Nexus1000v(horizon.Panel):
    name = _("Cisco Nexus 1000v")
    slug = 'nexus1000v'
    permissions = ('openstack.services.network',)

dashboard.Router.register(Nexus1000v)
