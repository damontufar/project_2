import PropTypes from 'prop-types'

const NewsButton = ({ color,text,onClick }) => {
    return (
        <button
            onClick={onClick}
            style={{ backgroundColor:color }}
            className='btn-news'
        >
            {text}
        </button>
    )
}

export default NewsButton
