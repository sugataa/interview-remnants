require 'net/http'
require 'json'

# Write a program that calculates how much it will cost you to buy all the clocks AND watches in the store
class ShopicruitCostCalculator
  attr_accessor :cost

  def initialize
    @cost = 0 # assume $0 to begin with
    base_url = 'http://shopicruit.myshopify.com/products.json?page='
    page_num = 1
    @has_products = true

    exec_parse(base_url, page_num) while @has_products
  end

  def exec_parse(base_url, page_num)
    hash_obj = get_products_hash(base_url, page_num)
    if hash_obj['products'] && !hash_obj['products'].empty?
      parse_prices(hash_obj['products'])
      page_num += 1
      exec_parse(base_url, page_num)
    else
      @has_products = false
    end
  end

  def parse_prices(products)
    products.each do |product|
      type = product['product_type']
      next unless (type == 'Clock') || (type == 'Watch')
      update_price(product['variants'])
    end
  end

  private

  def get_products_hash(base_url, page_num)
    url = base_url + page_num.to_s
    uri = URI(url)
    response = Net::HTTP.get(uri)
    hash_obj = JSON.parse(response)
    hash_obj
  end

  def update_price(variants)
    variants.each do |variant|
      @cost += variant['price'].to_f if variant['available'] == true
    end
  end
end

p "$#{ShopicruitCostCalculator.new.cost.round(2)}"
