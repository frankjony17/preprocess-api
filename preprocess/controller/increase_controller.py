import logging

from flask import Blueprint, jsonify, request

from preprocess.service.preprocess_service import PreprocessService
from preprocess.util.api_util import ApiUtil

increase_route = Blueprint('increase_route', __name__)


@increase_route.route("/image/increase-by-scale", methods=['POST'])
def image_increase():
    api_util = ApiUtil()
    service = PreprocessService()

    image_np, scale = api_util.is_valid_increase_request(request)

    increase_image_npa = service.increase_image(image_np, scale)
    increase_image_b64 = {
        'b64_image': service.np_array_to_base64(increase_image_npa)
    }
    logging.getLogger('ima_curio.controller').info('image rotate base64 -> OK')
    return jsonify(increase_image_b64), 200
