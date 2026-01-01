{# checks that there is no review date that is submitted before its listing was created:
 Make sure that every review_date in fct_reviews is more recent than the associated created_at in dim_listings_cleansed. #}
select * from {{ ref('fct_reviews') }} as reviews join {{ ref('dim_listings_cleansed') }} as listings using(listing_id)
  where listings.created_at > reviews.review_date
