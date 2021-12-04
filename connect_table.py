import boto3

dynamoDB = boto3.resource("dynamodb", aws_access_key_id="ASIARVMKPL5236LZNX5O",
                          aws_secret_access_key="SU+W+NCrhYdVX017z/N67LvNIcB2zS7y92jtS9vJ",
                          aws_session_token="FwoGZXIvYXdzEKj//////////wEaDLS8o/hPk4PgEjPs8iLKAbVvkgN8xg754vZ7Rt3L6GtsrNI4AZEFHXU628Vyx631mNVv7TSkgjAvQI4Yjlw24Mzm0iyFrlhJr5r9f0XV8Ob8PAPiftERnbGqzO7sFuRE2Hwkg5zPA82BQP1KIwcDyWBAIIpNQRNfib1C/IxQrS/v+fK8BoOqesGg6dR+z0uy3GLAvyS4NAaGuZWGJwMxSC0gPJn9ep3Gi+WnpIhFelaEHvOULVM1mEywQcPPND+yNC5qisAeUFsv8+BtK/+o5pVDOhxUDgEB/fso7435jAYyLVyXiDj9xCyZVKPpRTfHWbqcwW8vS8vgpwb5VpzQsPCGEYYoQBGr+7p3KuRAQQ==")

table1 = dynamoDB.Table('userTable')
table2 = dynamoDB.Table('recipeTable')
