import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


class Datasets:
    def __init__(self, team_id, project_id):
        self.team_id = team_id
        self.project_id = project_id
        self.validate()

    def validate(self):
        if type(self.team_id) != int:
            print(f"Team Id -{self.team_id} Should be Integer")
            return False, f"Team Id -{self.team_id}should be Integer"
        if type(self.project_id) != int:
            print(f"Project Id -{self.project_id} Should be Integer")
            return False, f"Project Id -{self.project_id} should be Integer"
        return True, "Success"

    def clear_values(self):
        self.team_id = None
        self.project_id = None

    def create(self, bucket_name, bucket_type=None):
        pass

    def get(self, bucket_name):
        pass

    @validate_access_key_and_token
    def list(self):

        status, response = self.validate()

        if not status:
            return response

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/datasets/?apikey={config.apikey}"

        headers['Authorization'] = f'Bearer {config.auth_token}'
        payload = ""

        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    def delete(self, bucket_name):
        pass

    @staticmethod
    def help():
        print("Datasets Class Help")
        print("\t\t=================")
        print("\t\tThis class provides functionalities to interact with Datasets.")
        print("\t\tAvailable methods:")
        print(
            "\t\t1. __init__(team_id, project_id): Initializes a Datasets instance with the specified team and "
            "project IDs.")
        print("\t\t2. create(bucket_name, bucket_type=None): Creates a new dataset with the provided bucket name and "
              "optional bucket type.")
        print("\t\t3. get(bucket_name): Retrieves information about a specific dataset using its bucket name.")
        print("\t\t4. list(): Lists all datasets associated with the team and project.")
        print("\t\t5. delete(bucket_name): Deletes a dataset with the given bucket name.")
        print("\t\t6. clear_values(): Resets the team and project IDs to None.")
        print("\t\t7. validate(): Checks if the team and project IDs are of integer type.")
        print("\t\t8. help(): Displays this help message.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\tdatasets = Datasets(123, 456)")
        print("\t\tdatasets.create('Bucket Name', 'Bucket Type')")
        print("\t\tdatasets.get('Bucket Name')")
        print("\t\tdatasets.list()")
        print("\t\tdatasets.delete('Bucket Name')")
