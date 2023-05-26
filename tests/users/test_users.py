import requests
from config import SERVICE_URL, SERVICE_URL1
from src.schemes.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schema.post import Post
from src.schemes.user import User


def test_getting_users_list(get_users):
    Response(get_users).assert_status_code(200).validate(User)


def test_another():
    assert 1 ==1

#z = [{"id":2146827,"name":"Bhoopat Mukhopadhyay","email":"bhoopat_mukhopadhyay@leffler.example","gender":"female","status":"inactive"},{"id":2146826,"name":"Deeptimoyee Nambeesan","email":"nambeesan_deeptimoyee@kirlin.test","gender":"female","status":"active"},{"id":2146825,"name":"Devika Dubashi","email":"devika_dubashi@mante.test","gender":"female","status":"active"},{"id":2146824,"name":"Ahilya Bhat","email":"ahilya_bhat@turner-ohara.example","gender":"female","status":"active"},{"id":2139740,"name":"Vedang Joshi","email":"vedang_joshi@crooks.example","gender":"male","status":"active"},{"id":2139739,"name":"Rep. Agnivesh Ganaka","email":"ganaka_agnivesh_rep@bednar.test","gender":"male","status":"inactive"},{"id":2139738,"name":"Msgr. Veda Guneta","email":"guneta_veda_msgr@stiedemann-leuschke.test","gender":"female","status":"inactive"},{"id":2139737,"name":"Vasudeva Iyer","email":"iyer_vasudeva@runolfsdottir.test","gender":"male","status":"inactive"},{"id":2139736,"name":"Rita Pothuvaal","email":"pothuvaal_rita@rowe.example","gender":"male","status":"inactive"},{"id":2139735,"name":"Chidaakaash Dutta","email":"dutta_chidaakaash@hammes.example","gender":"male","status":"active"}]


