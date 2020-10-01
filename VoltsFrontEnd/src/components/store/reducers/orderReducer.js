import {CREATE_ORDER_STATE, ORDER_RES} from "../types/types";

const initState = {
    order: [],
    res: {}
};

const orderReducer = (state=initState, action) => {
    switch (action.type) {
        case CREATE_ORDER_STATE:
            console.log('order persisted', action.payload);
            return {
              ...state,
              order: action.payload
            };
        case ORDER_RES:
            return {
              ...state,
                res: action.payload
            };

        default:
            return state

    }
};

export default orderReducer