import apiProvider from "ra-data-nestjsx-crud";
import { fetchUtils } from "ra-core";

const apiURL = import.meta.env.VITE_API_URL;
const baseDataProvider = apiProvider(apiURL);

export const dataProvider = {
  ...baseDataProvider,
  voidShipment: async (id: number): Promise<void> => {
    await fetchUtils.fetchJson(`${apiURL}/shipment/${id}/void`, {
      method: "POST",
    });
    return;
  },
  sendASN: async (id: number): Promise<void> => {
    await fetchUtils.fetchJson(`${apiURL}/shipment/${id}/asn`, {
      method: "POST",
    });
    return;
  },
  printTNTManifest: async (ids: number[]): Promise<Response> => {
    return fetch(`${apiURL}/tnt/manifest?ids=${ids.join(",")}`, {
      method: "GET",
      headers: {
        Accept: "application/pdf",
      },
    });
  },
};
