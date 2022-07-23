import logging

from flask import Blueprint, jsonify, request

from preprocess.service.preprocess_service import PreprocessService
from preprocess.util.api_util import ApiUtil

rotate_route = Blueprint('rotate_route', __name__)


@rotate_route.route("/image/rotate-by-angle", methods=['POST'])
def image_rotate():
    api_util = ApiUtil()
    service = PreprocessService()

    image_np, angle = api_util.is_valid_rotate_request(request)

    rotate_image_npa = service.rotate_image(image_np, angle)
    rotate_image_b64 = {
        'b64_image': service.np_array_to_base64(rotate_image_npa)
    }
    logging.getLogger('ima_curio.controller').info('image rotate base64 -> OK')
    return jsonify(rotate_image_b64), 200
