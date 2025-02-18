import { QuestionMarkCircleIcon } from '@heroicons/react/solid'
import { TicketIcon } from '@heroicons/react/outline'
import { Fragment } from 'react'
import { Link } from 'react-router-dom'
const ShippingForm = ({
    full_name,
    address_line_1,
    address_line_2,
    city,
    state_province_region,
    postal_zip_code,
    telephone_number,
    onChange,
    buy,
    user,
    renderShipping,
    total_amount,
    total_compare_amount,
    estimated_tax,
    shipping_cost,
    shipping_id,
    shipping,
    renderPaymentInfo,
    apply_coupon,
    coupon,
    coupon_name,
    total_after_coupon
}) => {
    return (
        <section
            aria-labelledby="summary-heading"
            className="mt-16 bg-gray-100 rounded-lg px-4 py-6 sm:p-6 lg:p-8 lg:mt-0 lg:col-span-5"
          >
            <h2 id="summary-heading" className="text-lg font-medium text-gray-900">
            Resumen del pedido
            </h2>

            <dl className="mt-6 space-y-4">
              <div className="flex items-center justify-between">
                {renderShipping()}
              </div>
              
              <div className="flex items-center justify-between">
                <form onSubmit={e => apply_coupon(e)}>
                    <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                        Cupón de descuento
                    </label>
                    <div className="mt-1 flex rounded-md shadow-sm">
                        <div className="relative flex items-stretch flex-grow focus-within:z-10">
                        
                        <input
                            name='coupon_name'
                            type='text'
                            onChange={e => onChange(e)}
                            value={coupon_name}
                            className="focus:ring-midnight-blue focus:border-midnight-blue block w-full rounded-none rounded-l-md pl-4 sm:text-sm border-gray-300"
                            placeholder="Ingrese código"
                        />
                        </div>
                        <button
                        type="submit"
                        className="-ml-px relative inline-flex items-center space-x-2 px-4 py-2 border border-gray-300 text-sm font-medium rounded-r-md text-gray-700 bg-gray-50 hover:bg-gray-100 focus:outline-none focus:ring-1 focus:ring-midnight-blue focus:border-midnight-blue"
                        >
                        <TicketIcon className="h-5 w-5 text-gray-400" aria-hidden="true" />
                        <span>Usar Cupón</span>
                        </button>
                        
                    </div>
                    
                </form>
              </div>

              {
                    coupon && 
                    coupon !== null &&
                    coupon !== undefined ? (
                        <div
                            className='text-green-500'
                        >
                            Cupón: {coupon.name} aplicado.
                        </div>
                    ) : (
                        <Fragment></Fragment>
                    )
                }

              <div className="border-t border-gray-200 pt-4 flex items-center justify-between">
                <dt className="flex items-center text-sm text-gray-600">
                  <span>Estimación de envío</span>
                  <Link to='' className="ml-2 flex-shrink-0 text-gray-400 hover:text-gray-500">
                    <span className="sr-only">Obtener más información sobre cómo se calcula el envío</span>
                    <QuestionMarkCircleIcon className="h-5 w-5" aria-hidden="true" />
                  </Link>
                </dt>
                <dd className="text-sm font-medium text-gray-900">{shipping && shipping_id !== 0 ? <>Bs{shipping_cost}</>:<div className="text-red-500">(Por favor seleccione la opción de envío)</div>}</dd>
              </div>

              <div className="border-t border-gray-200 pt-4 flex items-center justify-between">
                <dt className="flex text-sm text-gray-600">
                  <span>Estimación de Impuestos</span>
                  <Link to='' className="ml-2 flex-shrink-0 text-gray-400 hover:text-gray-500">
                    <span className="sr-only">Obtener más información sobre cómo se calculan los impuestos</span>
                    <QuestionMarkCircleIcon className="h-5 w-5" aria-hidden="true" />
                  </Link>
                </dt>
                <dd className="text-sm font-medium text-gray-900">{estimated_tax}Bs</dd>
              </div>
              
              <div className="border-t border-gray-200 pt-4 flex items-center justify-between">
                <dt className="flex text-sm text-gray-600">
                  <span>Subtotal</span>
                </dt>
                <dd className="text-sm font-medium text-gray-900">{total_compare_amount}Bs</dd>
              </div>

              {
                  coupon && 
                  coupon !== null && 
                  coupon !== undefined ?
                  <>
                    <div className="border-t border-gray-200 pt-4 flex items-center justify-between">
                        <dt className="flex text-sm text-gray-600">
                        <span>Descuento total: </span>
                        </dt>
                        <dd className="text-sm font-medium text-gray-900">{total_after_coupon}Bs</dd>
                    </div>
                    <div className="border-t border-gray-200 pt-4 flex items-center justify-between">
                        <dt className="text-base font-medium text-gray-900">Total del pedido</dt>
                        <dd className="text-base font-medium text-gray-900">{total_amount}Bs</dd>
                    </div>
                    </>
                        :
                    <div className="border-t border-gray-200 pt-4 flex items-center justify-between">
                        <dt className="text-base font-medium text-gray-900">Total del pedido</dt>
                        <dd className="text-base font-medium text-gray-900">{total_amount}Bs</dd>
                    </div>
              }
            </dl>

            <form onSubmit={e => buy(e)}>
                <div className=" px-4 py-5  mt-4 sm:px-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">Dirección de envío:</h3>
                </div>
                
                <div className="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-gray-200 sm:pt-5">
                    <label htmlFor="username" className="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                        Nombre completo
                    </label>
                    <div className="mt-1 sm:mt-0 sm:col-span-2">
                        <div className="max-w-lg flex rounded-md shadow-sm">
                        <input
                            type='text'
                            name='full_name'
                            placeholder={`${user.first_name} ${user.last_name}`}
                            onChange={e => onChange(e)}
                            value={full_name}
                            required
                            className="flex-1 block w-full focus:ring-midnight-blue focus:border-midnight-blue min-w-0 rounded-md sm:text-sm border-gray-300"
                        />
                        </div>
                    </div>
                </div>


                <div className="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-gray-200 sm:pt-5">
                    <label htmlFor="username" className="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2 ">
                        Dirección 1*
                    </label>
                    <div className="mt-1 sm:mt-0 sm:col-span-2">
                        <div className="max-w-lg flex rounded-md shadow-sm">
                        <input
                            type='text'
                            name='address_line_1'
                            onChange={e => onChange(e)}
                            value={address_line_1}
                            required
                            className="flex-1 block w-full focus:ring-midnight-blue focus:border-midnight-blue min-w-0 rounded-md sm:text-sm border-gray-300 mb-15"
                        />
                        </div>
                    </div>
                </div>

                <div className="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-gray-200 sm:pt-5">
                    <label htmlFor="username" className="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                        Dirección 2*
                    </label>
                    <div className="mt-1 sm:mt-0 sm:col-span-2">
                        <div className="max-w-lg flex rounded-md shadow-sm">
                        <input
                            type='text'
                            name='address_line_2'
                            onChange={e => onChange(e)}
                            value={address_line_2}
                            className="flex-1 block w-full focus:ring-midnight-blue focus:border-midnight-blue min-w-0 rounded-md sm:text-sm border-gray-300"
                        />
                        </div>
                    </div>
                </div>
                
                <div className="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-gray-200 sm:pt-5">
                    <label htmlFor="username" className="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                        Estado/Provincia*
                    </label>
                    <div className="mt-1 sm:mt-0 sm:col-span-2">
                        <div className="max-w-lg flex rounded-md shadow-sm">
                        <input
                            type='text'
                            name='state_province_region'
                            onChange={e => onChange(e)}
                            value={state_province_region}
                            required
                            className="flex-1 block w-full focus:ring-midnight-blue focus:border-midnight-blue min-w-0 rounded-md sm:text-sm border-gray-300"
                        />
                        </div>
                    </div>
                </div>
                
                <div className="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-gray-200 sm:pt-5">
                    <label htmlFor="username" className="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                        Código Postal
                    </label>
                    <div className="mt-1 sm:mt-0 sm:col-span-2">
                        <div className="max-w-lg flex rounded-md shadow-sm">
                        <input
                            type='text'
                            name='postal_zip_code'
                            onChange={e => onChange(e)}
                            value={postal_zip_code}
                            required
                            className="flex-1 block w-full focus:ring-midnight-blue focus:border-midnight-blue min-w-0 rounded-md sm:text-sm border-gray-300"
                        />
                        </div>
                    </div>
                </div>
                
                <div className="">
                    <label htmlFor="username" className="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                        Ciudad*
                    </label>
                    <div className="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-gray-200 sm:pt-5">
              <div className=" sm:col-span-2">
                <select
                  id='city'
                  name='city'
                  onChange={e => onChange(e)}
                  className="max-w-lg block focus:ring-midnight-blue focus:border-midnight-blue w-full shadow-sm sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
                >
                  {
                                city && 
                                city !== null &&
                                city !== undefined &&
                                city.map((country, index) => (
                                    <option key={index} value={country.name}>
                                        {country.name}
                                    </option>
                                ))
                            }
                </select>
              </div>
            </div>
                </div>

                <div className="sm:grid sm:grid-cols-3 mb-4 sm:gap-4 sm:items-start  sm:border-gray-200 sm:pt-5">
                    <label htmlFor="telephone_number" className="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                        Celular*
                    </label>
                    <div className="mt-1 sm:mt-0 sm:col-span-2">
                        <div className="max-w-lg flex rounded-md shadow-sm">
                        <input
                            type='tel'
                            name='telephone_number'
                            onChange={e => onChange(e)}
                            value={telephone_number}
                            required
                            className="flex-1 block w-full focus:ring-midnight-blue focus:border-midnight-blue min-w-0 rounded-md sm:text-sm border-gray-300"
                        />
                        </div>
                    </div>
                </div>
            {renderPaymentInfo()}
            </form>
          </section>
    )
}

export default ShippingForm;