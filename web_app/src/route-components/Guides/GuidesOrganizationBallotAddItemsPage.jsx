import axios from 'axios';
import BottomContinueNavigation from "components/navigation/BottomContinueNavigation";
import HeaderBackNavigation from "components/navigation/HeaderBackNavigation";
import React from "react";
import { Button, ButtonToolbar, Input, Navbar, ProgressBar } from "react-bootstrap";
import { Link } from "react-router";

export default class GuidesOrganizationBallotAddItemsPage extends React.Component {
	constructor(props) {
		super(props);
	}

	static getProps() {
		return {};
	}

	render() {
        var floatRight = {
            float: 'right'
        };
	    return (
<div>
    <HeaderBackNavigation header_text={"Create Voter Guide"} back_to_text={"< Back to Guides"} link_route={'guides_voter'} />
	<div className="container-fluid well well-90">
        <Link to="guides_organization_add_existing_link">
        </Link>

        <h4>Add More Ballot Items for your Guide</h4>
        <ProgressBar striped bsStyle="success" now={100} label="%(percent)s% Complete" />
        <p>Search for more ballot items to include.
        </p>
        <Input type="text" name="ballot_item_keyword" className="form-control"
               placeholder="Enter keywords, or a location" />
        <span style={floatRight}>
            <Link to="guides_organization_ballot_results" params={{guide_id: 27}}>
                <Button bsStyle="primary">Search</Button>
            </Link>
        </span>
        <br />
        <br />
	</div>
    <BottomContinueNavigation link_route_continue={'guides_organization_edit'} params={{guide_id: 27}} continue_text={'Continue >'} link_route_cancel={'guides_voter'} cancel_text={"cancel"} />
</div>
		);
	}
}
