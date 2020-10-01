import {GET_PRODUCTS_CATEGORIES} from '../types/types'


const initState = {
    categories: []
};

const categoryReducer = (state = initState, action) => {
    switch (action.type) {
        case GET_PRODUCTS_CATEGORIES:
            return {
                ...state,
                categories: action.payload
            };

        default:
            return state

    }
};

export default categoryReducer