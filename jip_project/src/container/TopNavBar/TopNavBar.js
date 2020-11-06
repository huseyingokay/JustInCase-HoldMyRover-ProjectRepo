import React, {Component} from 'react';
import classes from './TopNavBar.css';

class TopNavBar extends Component{
    render() {
        return(
            <div className="TopNavBar">
                {this.props.children}
            </div>
        )
    }    
}

export default TopNavBar;