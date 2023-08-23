from pymilvus import connections, list_collections
from Types import ConnectException


class MilvusConnection(object):
    uri = "127.0.0.1:19530"
    alias = "default"

    def connect(self, uri=None, username=None, password=None):
        self.uri = uri
        trimUsername = None if username is None else username.strip()
        trimPwd = None if password is None else password.strip()

        try:
            res = connections.connect(
                alias=self.alias, uri=self.uri, user=trimUsername, password=trimPwd
            )
            return res
        except Exception as e:
            raise ConnectException(f"Connect to Milvus error!{str(e)}")

    def showConnection(self, showAll=False):
        tempAlias = self.alias
        try:
            allConnections = connections.list_connections()

            if showAll:
                return allConnections

            aliasList = map(lambda x: x[0], allConnections)

            if tempAlias in aliasList:
                response = connections.get_connection_addr(tempAlias).values()
                return response
            else:
                return "Connection not found!"
        except Exception as e:
            raise Exception(f"Show connection error!{str(e)}")

    def disconnect(self):
        try:
            connections.disconnect(alias=self.alias)
            return f"Disconnect from {self.alias} successfully!"
        except Exception as e:
            raise Exception(f"Disconnect from {self.alias} error!{str(e)}")
