"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from GraphModel.Nodes.Node import Node


class NodeKnowledge(Node):
    """
    The `NodeKnowledge` class extends the functionality of the `Node` class by adding specific properties needed for
    representing knowledge in a graph model. It allows for nodes to be depicted with an additional description.
    """

    def __init__(self, description, titel, x=0, y=0):
        """
        Initializes a new instance of the Node class.

        :param: description: A string providing a description of the node.
        """
        super().__init__(titel, x, y)
        self.description = description
