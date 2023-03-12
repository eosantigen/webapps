# tarot.rb

require 'sinatra'

get '/symbol/:symbol' do
  "You selected symbol: #{params['symbol']}"
end

get '/spread/:spread_id' do
  "You selected spread: #{params['spread_id']}"
end
