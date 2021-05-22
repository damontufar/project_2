import PropTypes from 'prop-types'

const Header = ({ title }) => {
    return (
        <header className="header">
            <h1>{title}</h1>
        </header>
    )
}

Header.defaultProps = {
    title:'Global Health and Nutrition Metrics'
}

export default Header

