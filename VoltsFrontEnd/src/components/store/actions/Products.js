import React from "react";
import axios from 'axios'
import {GET_PRODUCTS_CATEGORIES, GET_SUBCATEGORY_PRODUCTS, GET_SUBCATEGORY_PRODUCTS_BY_NAME, GET_PRODUCT, CREATE_ORDER_STATE, ORDER_RES} from '../types/types'

export const get_products_categories = () => dispatch => {
    axios.get('api/product-categories/')
        .then(res => {
            dispatch({
                type: GET_PRODUCTS_CATEGORIES,
                payload: res.data
            })
        }).catch(err => console.log(err));
};

export const get_subcategory_products = (id) => dispatch => {
    //console.log('called', id);
    axios.get(`api/product-subcategories/${id}`)
        .then(res => {
            dispatch({
                type: GET_SUBCATEGORY_PRODUCTS,
                payload: res.data
            });
            //console.log('res',res.data)
        }).catch(err => console.log('error',err));
};

export const get_subcategory_products_by_name = (name) => dispatch => {
  axios.get(`api/product-subcategories-by-name/${name}`)
      .then(res => {
          dispatch({
              type: GET_SUBCATEGORY_PRODUCTS_BY_NAME,
              payload: res.data
          })
      })
};

export const get_product = (id) => dispatch => {
    axios.get(`api/products/${id}`)
        .then(res => {
            dispatch({
                type: GET_PRODUCT,
                payload: res.data
            });
        })

};

export const create_order = (order) => dispatch => {
    dispatch({
        type: CREATE_ORDER_STATE,
        payload: order
    })

};

export const post_order = (data) => dispatch => {
    axios.post('api/customer/',
        data).then(res => {
            dispatch({
                type: ORDER_RES,
                payload: res.data
            });
           // console.log(res.data);
    })
};