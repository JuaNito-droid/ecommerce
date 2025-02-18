import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/react/solid";

const Banner = ({ data = [] }) => {
  const [visibleIndex, setVisibleIndex] = useState(0);
  const [fade, setFade] = useState(false);
  const productsToShow = 5;
  const transitionTime = 8000;

  useEffect(() => {
    if (!Array.isArray(data) || data.length === 0) return;

    const interval = setInterval(() => {
      setFade(true);
      setTimeout(() => {
        setVisibleIndex((prevIndex) =>
          prevIndex + productsToShow >= data.length ? 0 : prevIndex + 1
        );
        setFade(false);
      }, 1200);
    }, transitionTime);

    return () => clearInterval(interval);
  }, [data]);

  if (!Array.isArray(data) || data.length === 0) {
    return (
      <div className="flex justify-center items-center h-[300px] p-8 bg-gray-100 rounded-lg border border-gray-200 shadow-lg">
        <div className="text-center">
          <p className="text-xl font-semibold text-gray-600 mb-4">
            ¡Ups! No hay productos disponibles en este momento.
          </p>
          <p className="text-md text-gray-500 mb-6">
            Estamos actualizando nuestra tienda. ¡Vuelve pronto para descubrir novedades!
          </p>
          <div className="mt-4">
            <Link
              to="/"
              className="inline-block px-6 py-3 bg-midnight-blue text-white rounded-md shadow-md hover:bg-purple-night transition"
            >
              Regresar al inicio
            </Link>
          </div>
        </div>
      </div>
    );
  }
  
  
  

  const visibleProducts = [
    ...data.slice(visibleIndex, visibleIndex + productsToShow),
    ...data.slice(0, Math.max(0, visibleIndex + productsToShow - data.length)),
  ];

  const handleNext = () => {
    setVisibleIndex((prevIndex) =>
      prevIndex + 1 >= data.length ? 0 : prevIndex + 1
    );
  };

  const handlePrev = () => {
    setVisibleIndex((prevIndex) =>
      prevIndex - 1 < 0 ? data.length - 1 : prevIndex - 1
    );
  };

  return (
    <div className="grid gap-4 p-8">
      <div className="hidden lg:block">
        {visibleProducts.length > 0 && (
          <>
            {/* Primera fila */}
            <div
              className={`flex transition-opacity duration-[1500ms] ${
                fade ? "opacity-0" : "opacity-100"
              }`}
            >
              <div className="w-1/2 p-2">
                <Link to={`product/${visibleProducts[0]?.id || "#"}`}>
                  <div className="relative w-full h-[180px] overflow-hidden rounded-lg m-2 group">
                    <img
                      src={visibleProducts[0]?.get_thumbnail || ""}
                      alt={visibleProducts[0]?.name || "Producto"}
                      className="absolute inset-0 w-full h-full object-contain rounded-lg transition-transform duration-500 group-hover:scale-105 group-hover:shadow-lg"
                    />
                    <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-30 transition-all duration-500 rounded-lg"></div>
                  </div>
                </Link>
              </div>
              <div className="w-1/2 p-2">
                <Link to={`product/${visibleProducts[1]?.id || "#"}`}>
                  <div className="relative w-full h-[260px] overflow-hidden rounded-lg m-2 group">
                    <img
                      src={visibleProducts[1]?.get_thumbnail || ""}
                      alt={visibleProducts[1]?.name || "Producto"}
                      className="absolute inset-0 w-full h-full object-contain rounded-lg transition-transform duration-500 group-hover:scale-105 group-hover:shadow-lg"
                    />
                    <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-30 transition-all duration-500 rounded-lg"></div>
                  </div>
                </Link>
              </div>
            </div>

            {/* Segunda fila */}
            <div
              className={`flex items-start transition-opacity duration-[1500ms] ${
                fade ? "opacity-0" : "opacity-100"
              }`}
            >
              <div className="w-1/4 p-2">
                <Link to={`product/${visibleProducts[2]?.id || "#"}`}>
                  <div className="relative w-full h-[280px] overflow-hidden rounded-lg m-2 group -mt-20">
                    <img
                      src={visibleProducts[2]?.get_thumbnail || ""}
                      alt={visibleProducts[2]?.name || "Producto"}
                      className="absolute inset-0 w-full h-full object-contain rounded-lg transition-transform duration-500 group-hover:scale-105 group-hover:shadow-lg"
                    />
                    <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-30 transition-all duration-500 rounded-lg"></div>
                  </div>
                </Link>
              </div>
              <div className="w-1/4 p-2">
                <Link to={`product/${visibleProducts[3]?.id || "#"}`}>
                  <div className="relative w-full h-[280px] overflow-hidden rounded-lg m-2 group -mt-20">
                    <img
                      src={visibleProducts[3]?.get_thumbnail || ""}
                      alt={visibleProducts[3]?.name || "Producto"}
                      className="absolute inset-0 w-full h-full object-contain rounded-lg transition-transform duration-500 group-hover:scale-105 group-hover:shadow-lg"
                    />
                    <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-30 transition-all duration-500 rounded-lg"></div>
                  </div>
                </Link>
              </div>
              <div className="w-1/2 p-2">
                <Link to={`product/${visibleProducts[4]?.id || "#"}`}>
                  <div className="relative w-full h-[200px] overflow-hidden rounded-lg m-2 group">
                    <img
                      src={visibleProducts[4]?.get_thumbnail || ""}
                      alt={visibleProducts[4]?.name || "Producto"}
                      className="absolute inset-0 w-full h-full object-contain rounded-lg transition-transform duration-500 group-hover:scale-105 group-hover:shadow-lg"
                    />
                    <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-30 transition-all duration-500 rounded-lg"></div>
                  </div>
                </Link>
              </div>
            </div>
          </>
        )}
      </div>

      {/* Carrusel para dispositivos móviles */}
      <div className="block lg:hidden">
        <div className="relative w-full h-[300px] overflow-hidden rounded-lg">
          <img
            src={data[visibleIndex]?.get_thumbnail || ""}
            alt={data[visibleIndex]?.name || "Producto"}
            className="absolute inset-0 w-full h-full object-cover rounded-lg transition-transform duration-500"
          />
          <div className="absolute inset-0 bg-black bg-opacity-0 transition-all duration-500"></div>

          <button
            onClick={handlePrev}
            className="absolute top-1/2 left-4 -translate-y-1/2 bg-gray-700 bg-opacity-50 hover:bg-opacity-75 text-white rounded-full p-2"
          >
            <ChevronLeftIcon className="h-6 w-6" />
          </button>
          <button
            onClick={handleNext}
            className="absolute top-1/2 right-4 -translate-y-1/2 bg-gray-700 bg-opacity-50 hover:bg-opacity-75 text-white rounded-full p-2"
          >
            <ChevronRightIcon className="h-6 w-6" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default Banner;
