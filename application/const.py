from application.models.attrdict import attrdict_const as dict


action = dict(
    abort = 'abort',
    alert = 'alert',
    redirect = 'redirect',
    none = None
)
message = dict(
    unexpected = 'Unexpected Error Occured',
    not_authorized = 'Not Authorized',
    result_none = 'DB : No Result Found',
    result_multiple = 'DB : Multiple Result Found'
)