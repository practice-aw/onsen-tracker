def data_org(yelp_info, all_data_dicts, yelp_ids):
    for data in yelp_info['businesses']:
        data_dict = {}
        data_dict['yelp_id'] = data['id']
        data_dict['name'] = data['name']
        data_dict['phone'] = data['phone']
        data_dict['is_closed'] = data['is_closed']
        data_dict['review_count'] = data['review_count']
        data_dict['yelp_rating'] = data['rating']
        data_dict['url'] = data['url']
        data_dict['latitude'] = data['coordinates']['latitude']
        data_dict['longitude'] = data['coordinates']['longitude']
        data_dict['image_url'] = data['image_url']
        a = ", "
        data_dict['address'] = a.join(data['location']['display_address'])
        data_dict['distance'] = data['distance']
        all_data_dicts.append(data_dict)
        yelp_ids.append(data['id'])
    return data_dict
#
# for data in business_data['businesses']:
#     data_dict = {}
#     data_dict['yelp_id'] = data['id']
#     data_dict['name'] = data['name']
#     data_dict['phone'] = data['phone']
#     data_dict['is_closed'] = data['is_closed']
#     data_dict['review_count'] = data['review_count']
#     data_dict['yelp_rating'] = data['rating']
#     data_dict['url'] = data['url']
#     data_dict['latitude'] = data['coordinates']['latitude']
#     data_dict['longitude'] = data['coordinates']['longitude']
#     data_dict['image_url'] = data['image_url']
#     a = ", "
#     data_dict['address'] = a.join(data['location']['display_address'])
#     data_dict['distance'] = data['distance']
#     all_data_dicts.append(data_dict)
#     yelp_ids.append(data['id'])
