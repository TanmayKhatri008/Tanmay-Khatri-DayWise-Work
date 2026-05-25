// Filter.jsx

export default function Filter({
    selectedCat,
    setSelectedCat,
    categories
}) {

    return (

        <section className="filters">

            <div className="categories">

                {categories.map((category) => (

                    <button
                        key={category}
                        onClick={() =>
                            setSelectedCat(category)
                        }

                        className={
                            selectedCat === category
                                ? "active-category"
                                : ""
                        }
                    >

                        {category}

                    </button>

                ))}

            </div>

        </section>

    );

}