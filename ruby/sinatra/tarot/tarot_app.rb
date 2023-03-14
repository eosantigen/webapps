# tarot.rb

require 'sinatra/base'

class Tarot_App < Sinatra::Base

  get '/symbol/:symbol' do
    symbol = params['symbol']
    puts "You selected symbol: #{symbol}"
    "you selected #{symbol}"
  end

  get '/spread/:spread' do
    spread = params['spread']
    puts "You selected spread: #{spread}"
  end

end
