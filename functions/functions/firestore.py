import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

GCP_CERTIFICATE = {
  "type": "service_account",
  "project_id": "buffme",
  "private_key_id": "e143aa60aa391f4e2aad235f7bd99a152da1d844",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDm8P2YbAAFx1g1\nTIO8kHJOXF0cuIK8ExKgYKbF3kgpPfjR5HhbU+p29y+dhmi+0zSWITa0PIP3lXlj\nQ1aG2njIjrTY0mEaem53M+A/NsHyQ/hfg8TbpnmtP/E35y3i0xS9Ze8Bv/Kdt3Je\nOV2OApGZD2H8/ToGl1716pK8xqiUmMQTaDemqeyvElotsVT/IvgKLKcM5UIE1Vxd\n+5rqmovQVwiC+Fhzg8S5NetYcecbS3Oh3YfVhqGQMxCCOEVHYV/0Sz5KC5frPtgW\nrpCFK/OcuncnVxpRRFzWia1Rtz+OBjWeyAbh0iFJDUjDY+Hp0Mv4CDLq184UaaJj\nkWGMv8JHAgMBAAECggEAAUI6/51HFFqVZOT5d6OjgkEHbBdzwindP7m6VV9ax7uQ\nvNDtkjUPSBeDNbnJasQLIbslaZVGDg/NTSwAYrr6GydVkQD3vbjN6Ied2npZhqqC\nktkZaS3etLUIHL5KOVXd/RJH9TVInnELhiJZG8o9ZOosJibZlB035UgI0k9hR9el\n3G1znrlMYYDX5UngI8a4L91+6SzC6AeEv8JkDt/PkvNVoq9j7sDRS5Cb3aAWqGtL\n2rC0i1dieoqKAqM3I1dI90Jg8wU2qAiRA9fauFs1naxwx4PC0TUDR+0PBRUMKOyA\nAmZN1UP9ckLA7X6ZFJg6bhCYGy6diZ1lGvCLzlGnEQKBgQD9YSia/WCByGiic4cZ\njSV9sXdbuAgk4DmrdIGK2qO57C0P16zV0k84sRu3uWgRRqNg1HIV27Zft83eIc82\nvZjap65lho6n8rYuHRYoyQx/4Mi7XUukZDtONskn0HiSxkXChIRGYwjD3mu72T/G\nlTjVt4Uh9CrVVY7MfX9HvHKOqwKBgQDpVGzfVKIRdR9l7jeK0R+eVcg7Xth4Bn1R\nri2mzmjhr5/yoohqcjn1ilI5eTrws29nGCCZN3/UrPOQtYjAc2f6chA6FxSIcqQB\nsLr5yaWisG/VDHPb3Ie0OOEZCoNyUb4PjiSf1g/zKtiZoxlf2dG1ilAzz76EMNst\n9F4bxhUq1QKBgCpllXvJpdpRhGCaYCLAYWOUzFoGgyZYdo3f4sUvLHIxuKCMABmP\nJT5hNDgbx/QME85h/ez2ZJ/Di6j9k0SfmPINWLsYNsqXbDBvIYQVkAfdvvjK9Zs+\nQkYmGKaW1XYJwyZ3MgLtE0xi7TfzdB5wXaA1Iwu5ZWlo9Yn1/dQtDiYdAoGBAK5h\n3ox64DVT54dypiglaxAW5HMay4XIs9hb6NqF4XTqoQvh1TpY7GBKZHF33UkPke7m\n5VYdWHhGWjKIug+7MLbIkMAZh8sCgviQcO1Ge3g/jRUZHW3wP6u95t2kMeE6nmVZ\nwp2CiqEeIIuSjeBJFqYrHQ3b8XMyYFzUCZGQVTmRAoGBAMXUmDeLe3Y8N81hZHTz\nb1fGrEPOkAt6erqyjRUfwjlp2HTETzbXchF1uaIcSSIsWXgwILl7Wv43pG2Q5jlK\nePsV+JArLPY3M3I92PQkKSSJzC9Ot3iLJqWcd+0v0k3TxCbajulzuvTKt0B8lRNG\nlHgMzLRUkIHH74u7zFovkxH8\n-----END PRIVATE KEY-----\n",
  "client_email": "buffme-firestore@buffme.iam.gserviceaccount.com",
  "client_id": "101915956475525422668",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/buffme-firestore%40buffme.iam.gserviceaccount.com"
}

cred = credentials.Certificate(GCP_CERTIFICATE)
firebase_admin.initialize_app(cred)

db = firestore.client()