import React, {Component, Fragment} from "react";
import {
    CardActionArea,
    Container,
    Grid,
    Card,
    Typography,
    CardMedia,
    CardContent,
    CardActions,
    Button,
} from "@material-ui/core";
import {connect} from 'react-redux'
import {Link,} from 'react-router-dom'
import './styles/subcategory.sass'
import {get_subcategory_products_by_name, get_product} from "../store/actions/Products";


class SubCategoriesProducts extends Component {
    constructor(props) {
        super(props);
        console.log('constr props',props);
        this.state = {
            products: props.subcategoryproducts.products
        };
        console.log('constr state', this.state);
        this.handleClick = this.handleClick.bind(this);
    }

    componentDidMount() {
        if(this.props.subcategoryproducts.length === 0){
            console.log('zero');
            const Subcategoryname = this.props.match.params.name;
            console.log(Subcategoryname);
            this.props.get_subcategory_products_by_name(Subcategoryname);
        }
    }

    handleClick = (id) => {
        console.log('id', id);
        this.props.get_product(id)

    };


    render() {
        const {products} = this.state;
        //console.log('propssssssssssss',this.props);
        return (
            <Fragment>
                <Typography className='subcategory_title' variant='h4'>{this.props.subcategoryproducts.name}</Typography>
                <Container className="products_container">
                    <Grid container spacing={4} style={{justifyContent: "space-evenly"}}>
                        {products && products.map(product => {
                            return (

                                <Grid item key={product.pk} xs={12} sm={12} md={9} style={{maxWidth: 345, minWidth: 250,}}>
                                    <Card style={{maxWidth: 345, minWidth: 250,}}>
                                        {console.log('product', product)}

                                        <Link to={'/details/' + product.pk} key={product.pk}>
                                            <CardActionArea onClick={this.handleClick.bind(this, product.pk)}>
                                                <CardMedia
                                                    component="img"
                                                    alt="Contemplative Reptile"
                                                    height="140"
                                                    src={product.product_image}
                                                    title="Contemplative Reptile"
                                                />
                                                <CardContent>
                                                    <Typography gutterBottom variant="h5" component="h2">
                                                        {product.product_name}
                                                    </Typography>
                                                    <Typography variant="body2" color="textSecondary" component="p">
                                                        Kshs. {product.product_price}
                                                    </Typography>
                                                </CardContent>
                                            </CardActionArea>
                                        </Link>
                                        <CardActions>
                                            <Button size="small" variant="contained" color="primary">
                                                Buy Now
                                            </Button>
                                            <Button onClick={this.props.handleAddToCart.bind(this, product)}
                                                    variant="outlined"
                                                    size="small"
                                                    color="primary">
                                                Add To Cart
                                            </Button>
                                        </CardActions>

                                    </Card>
                                </Grid>

                            )
                        })}
                    </Grid>
                </Container>

            </Fragment>
        )
    }
}

const mapStateToProps = (state, ownProps) => {
    console.log(ownProps);
    return {
        subcategoryproducts: state.products.SubCategories
    }

};

export default connect(mapStateToProps, {get_subcategory_products_by_name, get_product})(SubCategoriesProducts)